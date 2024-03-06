import { createQueue } from "kue";
import { expect } from 'chai';
import createPushNotificationsJobs from "./8-job.js";


const queue = createQueue();

describe("createPushNotificationsJobs", () => {
	before(() => {
		queue.testMode.enter();
	});

	after(() => {
		queue.testMode.clear();
		queue.testMode.exit();
	});

	beforeEach(() => {
		queue.testMode.clear();
	});

	it("Should create two push notification jobs with the correct data", () => {
		const users = [
			{ phoneNumber: "4153518780", message: "Hello, World!" },
			{ phoneNumber: "4153518781", message: "Hello, Kue!" },
		];

		createPushNotificationsJobs(users, queue);

		const jobs = queue.testMode.jobs;
		expect(jobs.length).to.equal(2);

		const job1 = jobs[0];
		expect(job1.type).to.equal("push_notification_code_3");
		expect(job1.data).to.deep.equal({
			phoneNumber: "4153518780",
			message: "Hello, World!",
		});

		const job2 = jobs[1];
		expect(job2.type).to.equal("push_notification_code_3");
		expect(job2.data).to.deep.equal({
			phoneNumber: "4153518781",
			message: "Hello, Kue!",
		});
	});

	it("Should not create any push notification jobs if the users array is empty", () => {
		const users = [];

		createPushNotificationsJobs(users, queue);

		const jobs = queue.testMode.jobs;
		expect(jobs.length).to.equal(0);
	});
});
