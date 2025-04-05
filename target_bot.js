require('dotenv').config();
const { chromium } = require('playwright');
const {Client, GatewayIntentBits} = require('discord.js');
const open = require('open');

const target_channel_id = '1355768964604755972';

let browser;
let page;

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

client.on('messageCreate', async (message) => {
    console.log(`Message received:  ${message.content}`);
    const linkRegex = /(https?:\/\/[^\s]+)/g;
    const  links = message.content.match(linkRegex);
    if(links && links.length > 0){
        for (const link of links){
            if(message.channel.id === target_channel_id){
                launch(link);
            }
        }
    }
});

client.once('ready', () => {
    console.log(`Target bot ${client.user.tag}`);
});

client.login(process.env.BOT_TOKEN);

async function launch(link){
    if(!browser){//open and login on the first ever link
        browser = await chromium.launch({ headless: false});
        console.log("HERE");
        //const context = await browser.newContext();
        page = await browser.newPage();
        login(page);
    }
    try{//redirect to new link
        await page.goto(link);
    } catch(err){
        console.error('Failed to open link ', err);
    }
}

async function login(page){
    await page.click('#account-sign-in');
    try{
        await page.click("//button[@data-test='accountNav-signIn']"); 
    }catch(err){
        console.log("second link doesn't pop up");
    }
    //await page.click("//button[@data-test='accountNav-signIn']");
    await page.fill('#username', 'carlos.arias2903@gmail.com');
    await page.fill('#password', 'Supersoaker1!');
    await page.click('#login');
}

