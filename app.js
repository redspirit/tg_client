const { TelegramClient } = require('telegram/gramjs');
const { functions, types } = require('telegram/gramjs/tl');

const apiId = 1902353;
const apiHash = '38306976eb0d10a6cbec59366fdd04b6';

(async () => {
    const client = new TelegramClient('session_name', apiId, apiHash);
    let cl = await client.start({
        // phone: '+79321232197',
        // code: () => { return '33355' }
    });

    // let result = await client.invoke(new functions.messages.SendMessageRequest({
    //     peer: 'GenerativeBeast2Bot',
    //     message: 'Hello there!'
    // }));

    const result = await client.invoke(new functions.messages.SendMessageRequest(
        peer='GenerativeBeast2Bot',
        message='Hello there!'
    ));

    console.log(result.stringify());
})();
