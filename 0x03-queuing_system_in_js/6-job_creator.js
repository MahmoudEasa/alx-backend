import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create("push_notification_code", {
    "phoneNumber": "0123456789",
    "message": "Hello SMSM",
});

job.on('complete', () => {
    console.log('Notification job completed');
    job.remove();
});

job.on('failed', () => {
    console.log('Notification job failed');
});

job.save((err) => {
    if (err) {
        console.error('Error creating notification job:', err);
    } else {
        console.log(`Notification job created: ${job.id}`);
    }
});
