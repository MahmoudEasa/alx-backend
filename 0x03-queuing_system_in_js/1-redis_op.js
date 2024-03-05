import redis, { createClient } from 'redis';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
    if (client)
        client.set(schoolName, value, (error, result) => {
            if (!error) redis.print("Reply: OK");
        });
}

const displaySchoolValue = (schoolName) => {
    if (client) client.get(schoolName, (error, result) => {
        if (!error) console.log(result);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
