# SilentSpeller: Towards mobile, hands-free, silent speech text entry using electropalatography
We’re sorry the repository is still under construction. We are confirming patent things.
This repository provides the entire pipeline for reproducing SilentSpeller results. Currently only the dataset of one of the participants and a python script to format the data are available, but soon we will provide a GT2K (HTK) based time series pattern recognition pipeline. This pipeline is useful for any time-series pattern recognition task. If you need it now, please contact us at kimura-naoki[at]g.ecc.u-tokyo.ac.jp.



# Overview
Speech is inappropriate in many situations, limiting when voice control can be used. Most unvoiced speech text entry systems can not be used while on-the-go due to movement artifacts. Using a dental retainer with capacitive touch sensors, SilentSpeller tracks tongue movement, enabling users to type by spelling words without voicing. SilentSpeller achieves an average 97% character accuracy in offline isolated word testing on a 1164-word dictionary. Walking has little effect on accuracy; average offline character accuracy was roughly equivalent on 107 phrases entered while walking (97.5%) or seated (96.5%). To demonstrate extensibility, the system was tested on 100 unseen words, leading to an average 94% accuracy. Live text entry speeds for seven participants averaged 37 words per minute at 87% accuracy. Comparing silent spelling to current practice suggests that SilentSpeller may be a viable alternative for silent mobile text entry.

Paper: https://dl.acm.org/doi/10.1145/3491102.3502015

Demo Video: https://youtu.be/eOFTN_sGgUI

10 min presentation: https://youtu.be/W1NpJ_bwiEU

## Data Preparation
Please download P1's dataset from the link below:
https://u.pcloud.link/publink/show?code=kZSLNFVZtSnyxYc4rVm0UBVdQKowhSiCDU4X

After downloading the dataset, run 220429_output_gt2k_dataset.py to make GT2k(HTK) styled dataset for training. You will get a folder named "gt2k_raw".

## Recognition part
###Dependencies

## Live text entry part
###Dependencies

### Baseline    

## Live Text Entry System

## References
Read the following paper for further details. If you use this code, please cite our work.


## Contact
kimura-naoki[at]g.ecc.u-tokyo.ac.jp
