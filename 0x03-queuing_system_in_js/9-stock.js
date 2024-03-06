import express from "express";
import redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const app = express();
const port = 1245;

const listProducts = [
    {'Id': 1, 'name': 'Suitcase 250', 'price': 50, 'stock': 4},
    {'Id': 2, 'name': 'Suitcase 450', 'price': 100, 'stock': 10},
    {'Id': 3, 'name': 'Suitcase 650', 'price': 350, 'stock': 2},
    {'Id': 4, 'name': 'Suitcase 1050', 'price': 550, 'stock': 5},
    {'Id': 5, 'name': 'Suitcase 1000', 'price': 1000, 'stock': 0},
];

// listProducts.map(el => client.del(`item.${el.Id}`))

const isEmpty = (obj) => Object.keys(obj).length === 0;

const getItemById = (id) => {
    const product = listProducts.filter((e) => e.Id === id);
    return (product);
}

const reserveStockById = async (itemId, stock) => {
    try {
        const promisifiedGet = promisify(client.set).bind(client);
        const redisKey = `item.${itemId}`;
    
        await promisifiedGet(redisKey, JSON.stringify(stock));
        redis.print("Reply: OK");
    } catch (err) {
		console.log(err);
	}
}

// listProducts.map(el => reserveStockById(el.Id, JSON.stringify(el)));

const getCurrentReservedStockById = async (itemId) => {
    try {
        const redisKey = `item.${itemId}`;
        const promisifiedGet = promisify(client.get).bind(client);
		const client_get = await promisifiedGet(redisKey);
        return (client_get);
	} catch (err) {
		console.log(err);
	}
}

app.get('/list_products', (req, res) => {
    const data = listProducts.map(el => {
        return ({
            "itemId": el.Id,
            "itemName": el.name,
            "price": el.price,
            "initialAvailableQuantity": el.stock,
        });
    });
    res.json(data);
});

app.get('/list_products/:itemId', async (req, res) => {
    try {
        const id = req.params.itemId;
        let data = await getCurrentReservedStockById(id);
        if (!data || isEmpty(data)) res.json({"status": "Product not found"});
        else {
            data = JSON.parse(data);
            const result = {
                "itemId": data.Id,
                "itemName": data.name,
                "price": data.price,
                "initialAvailableQuantity": data.stock,
                "currentQuantity": data.stock
            };
            res.json(result);
        }
    } catch (err) {
		console.log(err);
	}
});

app.get('/reserve_product/:itemId', async (req, res) => {
    try {
        const id = +req.params.itemId;
        let data = getItemById(id);
    
        if (!data.length) res.json({"status":"Product not found"});
        else {
            data = data[0];
        
            if (!data.stock) res.json(
                {"status": "Not enough stock available", "itemId": data.Id}
                );
            else {
                await reserveStockById(id, data);
                res.json({"status": "Reservation confirmed","itemId": id});
            }
        }
    } catch (err) {
		console.log(err);
	}
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
