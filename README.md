# STEPS:
## This is a way to interact with bundlr using the CLI. Bundlr has a JS Client method for interaction.
### Check out the bundlr docs. Super easy to understand... 
[Bundlr Docs](https://docs.bundlr.network/)

Note: I'm not going to be explaining brownie here, its basically a framework for scripting and testing your smart contracts like hardhat. Instead I'll explain some part of the NFT(Unrelated NFT's) contract. You could easily modify the contract to fit your needs and test with a framework of your choice as I'll be focusing on using bundlr itself to store data permanently on arweave.

1. Install bundlr 
```
npm install -g @bundlr-network/client
```
2. For Testing Bundlr has a devnet that you could use, Its compatible with the supported networks on mainnet. To work with bundlr devnet make use of "https://devnet.bundlr.network" and set a provider url for the respective testnet. For this example I'd be using Alchemy and Mumbai tesntet (matic). If you'd like to go mainnet use "https://node1.bundlr.network". Feel free to use whatever you like...

3. Note: Anything stored on the devnet never actually moves to arweave and will be cleared from bundlr after a week.

4. To check your bundlr balance run the code below in your terminal. Your initial balance should be 0. Till you fund the a bundlr node. In this example I use matic(test-matic). You could check out the docs for other [Supported Currencies](https://docs.bundlr.network/docs/currencies)
```
bundlr balance "YOUR ADDRESS" -h "https://devnet.bundlr.network" -c "matic"
```
You should get:
```
Balance: 0 wei (0 matic)
```

5. Then fund a bundlr node. In this example I'm using 0.3 matic in atomic units(Wei i.e 10^18). If you're funding with Arweave its 10^12
```
bundlr fund 300000000000000000 -h "https://devnet.bundlr.network" -w "YOUR PRIVATE KEY" -c "matic" --provider-url "https://polygon-mumbai.g.alchemy.com/v2/YOUR_ALCHEMY_APP_ID"
```
You'll be prompted with a Y/N
enter Y
There's usually a fee. ON devnet its zero.
Then check your balance again!
Congrats! Time to for the good stuff...

6. Prepare a metadata folder and images folder for storing all your images and metadata(.json). Make sure the folders are in the same directory you installed bundlr. You could upload a folder or a single file using bundlr. For this example we'll be using a folder named "images" containing our images which we stored as 1.jpg, 2.jpg, 3.jpg e.t.c The same for our metadata saved as "metadata" with files 1.json, 2.json, 3.json e.t.c

7. Upload your images folder FIRST with bundlr
```
bundlr upload-dir images -h "https://devnet.bundlr.network" -w "YOUR PRIVATE KEY" -c "matic"
```
A manifest file will show up everytime you upload a folder
Bundlr will show you the total amount of data and its cost before you confirm the upload!
Bundlr will then return a link to where the folder lives on the arweave network. In a format like so:
```
https://arweave.net/SOME_LONG_ID
```

You'll be able to use this to access every individual image by going to your browser and typing
"https://arweave.net/SOME_LONG_ID/imagename.format"
E.g
"https://arweave.net/19082991010hxjnc_gshcuw89/1.jpg"
Note:These are just examples that dont lead to anywhere

8. Once this is done go to each individual json file in your metadata folder and update the "image" part to be the link gotten from arweave with respective destinations. E.g "https://arweave.net/19082991010hxjnc_gshcuw89/1.jpg" for 1.json e.t.c
This is essential!
After succesfully updating the the imageURI.
Go on ahead and and upload the "metadata" folder with
```
bundlr upload-dir metadata -h "https://devnet.bundlr.network" -w "YOUR PRIVATE KEY" -c "matic"
```
Nice work!

8. If you'd like to you could check your balance again and see how much tokens you spent on uploading both those folder to arweave PERMANENTLY. Haha! obviously ours isn't permanent because we're on the devnet. But it could be! if you tweak a few things and use actual money! ;D

9. We could also check the price of how much data we want to store in bytes before uploading e.g 1mb
```
bundlr price 1000000 -h "https://devnet.bundlr.network" -c "matic"
```
Price for 1000000 bytes in matic is 9916924873158020 wei (0.00991692487315802 matic)

10. You can now check balance and Withdraw your testnet funds using:
```
bundlr withdraw AMOUNT_IN_WEI -h "https://devnet.bundlr.network" -w "PRIVATE_KEY" -c "matic"
```

11. Final Bit.... Check out the contract and update the baseURI to be equal to our metadata link from arweave with a "/" at the end. The contract automatically concatenates the tokenId and the json part.

12. You're all done!...You dont't have to worry about pinning, your image is stored FOREVER??!. Thanks and I'd appreciate a follow and a star on this repository!. :cowboy_hat_face:

13. Oh and I used my test metamaks for this, I'd advise you do the same to get used to it first. Also I got all these images from [pexels](https://www.pexels.com/)! The images should stop persisting after a week or so on the opensea testnet because I uploaded it via bundlrs devnet not mainnet. Here's the link to the collection. [UNRELATED](https://testnets.opensea.io/collection/unrelated-v3). :grinning: 	


