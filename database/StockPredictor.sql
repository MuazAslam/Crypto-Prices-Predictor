CREATE DATABASE StockPredictor;
USE StockPredictor;

CREATE TABLE Users (
    User_ID INT IDENTITY(1,1) PRIMARY KEY,
    User_Name VARCHAR(100) NOT NULL,
    User_Email VARCHAR(100) NOT NULL UNIQUE,
    User_Phone VARCHAR(15) NOT NULL UNIQUE,
    User_Password VARCHAR(255) NOT NULL
);


CREATE TABLE Cryptocurrencies (
    Crypto_ID INT IDENTITY(1,1) PRIMARY KEY,
    Symbol VARCHAR(10) UNIQUE NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Description TEXT,
    Launch_Date DATE
);

CREATE TABLE Recent_Stocks (
	Recent_ID INT IDENTITY(1,1) PRIMARY KEY,
    Crypto_ID INT,
    Price_Date DATE NOT NULL,
    Open_Price DECIMAL(15,2),
    Close_Price DECIMAL(15,2),
    High_Price DECIMAL(15,2),
    Low_Price DECIMAL(15,2),
    Volume DECIMAL(20,2),
    FOREIGN KEY (Crypto_ID) REFERENCES Cryptocurrencies(Crypto_ID)
);

CREATE TABLE User_Recent_Views (
    User_ID INT,
    Recent_ID INT,
	Viewed_At DATETIME DEFAULT GETDATE(),
    PRIMARY KEY (User_ID, Recent_ID),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
    FOREIGN KEY (Recent_ID) REFERENCES Recent_Stocks(Recent_ID)
);

SELECT * FROM Users

INSERT INTO Cryptocurrencies (Symbol, Name, Description, Launch_Date) VALUES
('XEM-USD', 'NEM', 'A blockchain platform focused on enterprise applications and smart assets.', '2015-03-31'),
('TRB-USD', 'Tellor', 'A decentralized oracle network for feeding real-world data to smart contracts.', '2018-07-01'),
('CRO-USD', 'Crypto.com Coin', 'The native cryptocurrency of Crypto.com, a global crypto exchange.', '2018-11-14'),
('MKR-USD', 'Maker', 'A decentralized autonomous organization that manages the Dai stablecoin and its ecosystem.', '2015-12-01'),
('BNT-USD', 'Bancor', 'A decentralized liquidity network enabling token swaps on Ethereum and other blockchains.', '2017-01-01'),
('AAVE-USD', 'Aave', 'A decentralized finance platform offering lending and borrowing services for digital assets.', '2017-11-01'),
('ALGO-USD', 'Algorand', 'A high-performance blockchain platform designed for speed and scalability.', '2019-06-19'),
('STPT-USD', 'Standard Protocol', 'A decentralized protocol for business and financial applications using blockchain technology.', '2020-09-01'),
('SUSHI-USD', 'SushiSwap', 'A decentralized exchange and automated market maker (AMM) built on Ethereum.', '2020-08-28'),
('FTM-USD', 'Fantom', 'A fast, scalable, and secure blockchain platform for decentralized applications and cryptocurrencies.', '2018-12-15'),
('LRC-USD', 'Loopring', 'A layer-2 decentralized exchange and payment protocol for the Ethereum blockchain.', '2017-08-01'),
('XMR-USD', 'Monero', 'A privacy-focused cryptocurrency that uses advanced cryptography to obfuscate transactions.', '2014-04-18'),
('STMX-USD', 'StormX', 'A decentralized rewards platform that allows users to earn cryptocurrency through shopping.', '2015-08-18'),
('CTSI-USD', 'Cartesi', 'A layer-2 platform that brings Linux and standard software to smart contracts.', '2018-05-01'),
('KNC-USD', 'Kyber Network', 'A decentralized liquidity protocol that connects liquidity providers with users in DeFi ecosystems.', '2017-09-15'),
('FTT-USD', 'FTX Token', 'The native token of the FTX crypto exchange, used for trading fee discounts and more.', '2019-07-08'),
('OCEAN-USD', 'Ocean Protocol', 'A decentralized data exchange protocol that unlocks data for AI consumption.', '2017-01-01');




INSERT INTO Cryptocurrencies (Symbol, Name, Description, Launch_Date) VALUES
('BTC-USD', 'Bitcoin', 'The first decentralized cryptocurrency, enabling peer-to-peer transactions without intermediaries.', '2009-01-03'),
('ETH-USD', 'Ethereum', 'A decentralized platform for smart contracts and decentralized applications (dApps).', '2015-07-30'),
('USDT-USD', 'Tether', 'A stablecoin pegged to the US dollar, facilitating stable digital transactions.', '2014-10-06'),
('BNB-USD', 'Binance Coin', 'The native token of Binance exchange, used for trading fee discounts and more.', '2017-07-25'),
('SOL-USD', 'Solana', 'A high-performance blockchain supporting scalable decentralized applications.', '2020-03-20'),
('XRP-USD', 'XRP', 'A digital asset designed for fast and cost-efficient cross-border payments.', '2012-06-02'),
('USDC-USD', 'USD Coin', 'A fully-backed US dollar stablecoin issued by regulated financial institutions.', '2018-09-10'),
('DOGE-USD', 'Dogecoin', 'A meme-inspired cryptocurrency known for its active community and tipping culture.', '2013-12-06'),
('ADA-USD', 'Cardano', 'A research-driven blockchain platform for smart contracts and decentralized applications.', '2017-10-01'),
('AVAX-USD', 'Avalanche', 'A scalable and secure platform for decentralized applications and custom blockchains.', '2020-09-21'),
('TON-USD', 'Toncoin', 'The native token of The Open Network, aiming to integrate blockchain with Telegram.', '2021-05-07'),
('SHIB-USD', 'Shiba Inu', 'A meme token and Dogecoin competitor with a growing decentralized ecosystem.', '2020-08-01'),
('WTRX-USD', 'Wrapped TRON', 'An ERC-20 token representing TRON, enabling its use on the Ethereum network.', '2020-12-24'),
('DOT-USD', 'Polkadot', 'A multi-chain platform enabling interoperability between different blockchains.', '2020-05-26'),
('WBTC-USD', 'Wrapped Bitcoin', 'An ERC-20 token backed 1:1 with Bitcoin, bringing BTC to Ethereum.', '2019-01-30'),
('TRX-USD', 'TRON', 'A blockchain platform focused on decentralized content sharing and entertainment.', '2017-09-13'),
('LINK-USD', 'Chainlink', 'A decentralized oracle network connecting smart contracts with real-world data.', '2017-09-19'),
('BCH-USD', 'Bitcoin Cash', 'A Bitcoin fork offering larger block sizes for faster transactions.', '2017-08-01'),
('NEAR-USD', 'NEAR Protocol', 'A scalable blockchain platform for decentralized applications with user-friendly features.', '2020-04-22'),
('LTC-USD', 'Litecoin', 'A peer-to-peer cryptocurrency offering faster transaction confirmation times.', '2011-10-13');
