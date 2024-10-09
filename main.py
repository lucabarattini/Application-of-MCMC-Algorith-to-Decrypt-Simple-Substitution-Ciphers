from decrypt import mcmc

def main():
    '''
    Testing the MCMC chain
    '''

    try: mcmc.mcmc_decrypt( 2000,
                            "ciphertext.txt",
                            "corpus.txt",
                            n= 2)

    except Exception as e:
        print(e)


main()
