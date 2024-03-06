import express from "express";
import { promisify } from 'util';
import { createQueue } from 'kue';
import redis, { createClient } from 'redis';

const app = express();
const client = createClient();
const queue = createQueue();
const port = 1245;
let reservationEnabled = true;


const reserveSeat = async (number) => {
    try {
        const promisifiedGet = promisify(client.set).bind(client);
    
        await promisifiedGet('available_seats', number);
        redis.print("Reply: OK");
    } catch (err) {
		console.log(err);
	}
}

const getCurrentAvailableSeats = async () => {
    try {
        const promisifiedGet = promisify(client.get).bind(client);
		const client_get = await promisifiedGet('available_seats');
        return (client_get);
	} catch (err) {
		console.log(err);
	}
}

app.get('/available_seats', async (req, res) => {
    try {
        const data = await getCurrentAvailableSeats();
        res.json({"numberOfAvailableSeats": data});
    } catch (err) {
		console.log(err);
	}
});

app.get('/reserve_seat', (req, res) => {
    try {
        if (!reservationEnabled) res.json({ "status": "Reservation are blocked" });
        else {
            const job = queue.create('reserve_seat');
    
            job.on('complete', () => {
                console.log(`Seat reservation job ${job.id} completed`);
                job.remove();
            });
            
            job.on('failed', (err) =>
                console.log(`Seat reservation job ${job.id} failed: ${err}`));
        
            job.save((err) => {
                if (err) res.json({ "status": "Reservation failed" });
                else res.json({ "status": "Reservation in process" });
            });
        }
    } catch (err) {
		console.log(err);
	}
});

app.get('/process', async (req, res) => {
    try {
        queue.process('reserve_seat', async (job, done) => {
            let currentAvailableSeats = await getCurrentAvailableSeats();
            currentAvailableSeats = +currentAvailableSeats;
    
            if (currentAvailableSeats === 1) reservationEnabled = false;
            if (currentAvailableSeats < 0) done(new Error('Not enough seats available'));
            reserveSeat(currentAvailableSeats - 1);
            done();
        });
        
        res.json({ "status": "Queue processing" });
    } catch (err) {
		console.log(err);
	}
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
    reserveSeat(50);
});
