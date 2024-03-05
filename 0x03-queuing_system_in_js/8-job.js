const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

    for (const el of jobs) {
        const job = queue.create("push_notification_code_3", el);
    
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
            job.remove();
        });
        
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        });
    
        job.on('progress', (process) => console.log(`Notification job ${job.id} ${process}% complete`));
        
        job.save((err) => {
            if (err) console.error('Error creating notification job:', err);
            else console.log(`Notification job created: ${job.id}`);
        });
    }
}
export default createPushNotificationsJobs;
