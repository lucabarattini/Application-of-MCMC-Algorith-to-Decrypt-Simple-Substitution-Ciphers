<div align="center">

# 🔐 MCMC Decryption Project
### Breaking Simple Substitution Ciphers with MCMC Chain

<br>

![Python](https://img.shields.io/badge/Python-3.14+-blue?style=for-the-badge&logo=python&logoColor=white)
![MCMC](https://img.shields.io/badge/Algorithm-MCMC-orange?style=for-the-badge)
![Security](https://img.shields.io/badge/Context-Cryptography-red?style=for-the-badge)

</div>

---

### 👨‍💻 Team Members
* **Simone Di Lorenzo**
* **Luca Barattini**

---

### 📜 Overview
This project utilizes the **Markov Chain Monte Carlo (MCMC)** algorithm to decrypt substitution ciphertexts without a known key.

The core logic relies on a custom `log_likelihood` function to score the "English-ness" of a decrypted text sequence, optimizing the cipher key through thousands of iterations to find the readable text.

---

### 🚀 Quick Start

#### 1. Clone the Repository:
```bash
git clone [https://github.com/lucabarattini/YOUR-REPO-NAME.git](https://github.com/lucabarattini/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME
```

### 2. Setup Files:
Ensure the following files are located in the root directory alongside main.py:

📄 ciphertext.txt: The secret message you wish to decrypt.

📚 corpus.txt: Reference text used for language modeling (e.g., War and Peace, or a standard dictionary).

### 3. Run the Decryption:
Execute the main script to start the MCMC process:

```bash
python main.py
```

### 3. Paper where we present the project:

<div align="center">

<img src="/img/Application of MCMC to decrypt subst cipher-01.png" width="100%" alt="Slide 1" />



<img src="/img/Application of MCMC to decrypt subst cipher-02.png" width="100%" alt="Slide 2" />



<img src="/img/Application of MCMC to decrypt subst cipher-03.png" width="100%" alt="Slide 3" />



<img src="/img/Application of MCMC to decrypt subst cipher-04.png" width="100%" alt="Slide 4" />



<img src="/img/Application of MCMC to decrypt subst cipher-05.png" width="100%" alt="Slide 5" />



<img src="/img/Application of MCMC to decrypt subst cipher-06.png" width="100%" alt="Slide 6" />



<img src="/img/Application of MCMC to decrypt subst cipher-07.png" width="100%" alt="Slide 7" />



<img src="/img/Application of MCMC to decrypt subst cipher-08.png" width="100%" alt="Slide 8" />



<img src="/img/Application of MCMC to decrypt subst cipher-09.png" width="100%" alt="Slide 9" />

</div>

### 📬 Contact:
For more info, feel free to reach out:

📧 Simone: simone@dilorenzo.com

📧 Luca: lb3656@columbia.edu
