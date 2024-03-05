import { createQueue } from 'kue';

const queue = createQueue();
const  blacklistedPhoneNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0);
    if (blacklistedPhoneNumbers.includes(phoneNumber)) {
        const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
        done(new Error(errorMessage));
    }
    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    job.progress(0, 100);
    sendNotification(phoneNumber, message, job, done);
});
