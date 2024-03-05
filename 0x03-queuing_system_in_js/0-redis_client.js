import { createClient } from 'redis';

(async () => {
    try {
        const client = await createClient();
        client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
        client.on('connect', () => console.log('Redis client connected to the server'));
    } catch (error) {
        console.error('Redis client not connected to the server: ', error);
    }
})();
