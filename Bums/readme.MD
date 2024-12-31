📞 Contact

> [Termux guides if you run on mobile](https://github.com/MeoMunDep/Guides-for-using-my-script-on-termux.)


> If you encounter any issues or have questions, feel free to reach out:

- Contact: [Link](t.me/MeoMunDep)
- Group: [Link](t.me/KeoAirDropFreeNe)
- Channel: [Link](t.me/KeoAirDropFreeNee)

> > > Help me with your referral [Link](https://t.me/bums/app?startapp=ref_OVMEplvN-go_ganginfo_1854937255193260033
)

## 🚀 Getting Started

To get started with the bot, follow these steps:

0. **Dowload NodeJS to run the bot**
> Remember to download Nodejs version: **22.11.0** and NPM version: **10.9.0**

> > [Download Link](https://t.me/KeoAirDropFreeNe/257/1462)

-> Double click on setup.bat or setup.sh if you want to run automatically, remember to fill all the necessary data.

1. **Install Dependencies and Modules:**

   ```
   npm i user-agents cloudscraper axios colors p-limit https-proxy-agent socks-proxy-agent
   ```

2. **Prepare Configuration Files:**

   > You'll need to set up a few configuration files for the bot to work properly.

## 📁 Configuration Files

### 1. `configs.json` 📜 - Adjust configuration

```json
{
  "limit": 100,
  "countdown": 300,
  "country_time": "en-US",
  "delayEachAccount": [5, 8],
  "isSkipInvalidProxy": false,
  "howManyEnergyUpgrade": 10,
  "howManyRecoveryUpgrade": 10,
  "howManyTapUpgrade": 10,
  "howManyBonusChanceUpgrade": 10,
  "howManyBonusRatioUpgrade": 10,
  "maxCardPrice": 1000000,
  "combo": "101,102,103",
  "isDoTasks": true,
  "howManyTapsInOneTime": [10, 100],
  "isBuyBoosts": true,
  "isUpgradeCards": true,
  "infinityTapping": true,
  "trackingTapPoints": true,
  "openNoelGifts": true
}

```

### 2. `datas.txt` 🗂️ -

```txt
query_id.../user...
query_id.../user...
query_id.../user...
```

### 3. `wallets.txt` 💼 - Cannot update yet.

```txt - wallet address
abc...xyz
abc...xyz
abc...xyz
```

### 4. `proxies.txt` 🌐 - Proxy is an option. If you have one, fill it in; otherwise, leave it blank.

```txt
http://user:password@host:port
https://user:password@host:port
socks4://user:password@host:port
socks5://user:password@host:port
```

### 5. `answers.txt` 🌐 - Fill with youtube's tasks answers.

```txt
xxx...
xxx...
xxx...
```

💡 Usage:

> You need to `cd` to the file after extract it
> To run the bot, use the following command: `cd bums-main/bums; node 1`

🎇Enjoy!
