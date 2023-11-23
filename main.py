import frequencyanalysis
import cipher
import MCMC
import scoring_function

#test

def main():
    '''
    Testing the MCMC chain
    '''

    try: MCMC.mcmc_decrypt( 100, 
                            "plaintext.txt", 
                            "ciphertext.txt",
                            "final_cipher.txt",
                            "final_decryption.txt")

    except Exception as e:
        print(e)


main()
