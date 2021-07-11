# API Poisoning

Theoritical scenario in which it may be necessary to disrupt data collection of an on going phishing attempt
------------------------------------------------------------------------------------------------------------

request_spammer.py
------------------
Sends post requests with fake credentials generated from various wordlists
in order to poison the malicious actors stolen data pool.

1. The API endpoint was found through inspecting the network traffic in a web browser while submitting fake data.
2. Postman was used to construct/verify identical POST request headers and payload.
3. Once a valid POST request was confirmed, a quick python script was written to spam the malicious actors API with fake credentials.
* This method of attack was a success! Not only was their data pool tainted with hundreds of thousands of fake credentials,
  the massive amount of requests resulted in a Denial of Service by using up all the endpoint servers bandwidth and shutting it down..for now.
  
Usage
-----
1. Clone this repo:  
`git clone https://github.com/chparmley/Phishing_Counter_Attack.git`  
2. Extract ./Phishing_Counter_Attack/wordlist/rockyou.zip  
3. Open terminal inside the Phishing_Couter_Attack folder and run with:  
`python3 request_spammer.py`


