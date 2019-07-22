## Table of Contents

- [Table of Contents](#table-of-contents)
- [Summary](#summary)
- [Methodology](#methodology)
	- [Wrangling](#wrangling)
	- [Feature Engineering](#feature-engineering)
	- [Model Stacking](#model-stacking)
- [Discussion](#discussion)
- [Key Learnings from the Winners](#key-learnings-from-the-winners)

## Context

This is the repo for the 2019 UNSW Data Science Hackathon.

We were tasked to build a model to predict which patients have a risk for stroke given their attributes. 

I entered this competition solo, and tried to build a rather complicated stacking model inspired by some Kaggler winners' solutions that I had studied prior to the competition.  

Unfortunately the results were not optimal given the dataset. The higher placing competitors in the private leaderboard used few models with hyperparameter tuning and feature engineering.

---

## Methodology

### Wrangling

The data was quite messy. We separated the any variables that were concatenated into 1 column, and corrected any misformatted strings and removed undecipherable and missing values.

`smoker_status` had the greatest number of missing variables. 

I dropped the `treatment` variables but in hindsight they should have been kept, as non-treatments would just warrant a negative response. For some reason this possibility eluded me.  

There were no obvious outliers and thus I did not clip the continuous variables to a 95% quantile, but I did normalise the continuous variables. s

### Feature Engineering

Categorical variables were handled via one-hot encoding, and extra features were created by binning BMI, average blood sugar and age. We also tried to combine the smoker_status variable. 

The imbalanced dataset was handled with SMOTE-NC upsampling to 20% of the original dataset size. 

### Model Stacking

I tried an approach I read from a Github repo, doing feature selection with linear and tree models. These features were then used to build the baseline models which were stacked and trained by a 2nd XGBoost. 

We evaluated using ROC-AUC due to the imbalanced dataset. 

The results were suboptimal. 

I tried the same procedure using only the base features and none of the engineered features but the result was similar or worse.

I also attempted upsampling the data to 10 and 30% of the original sample size, but could not obtain any improvements. 

---

## Discussion

In hindsight, the best approach would have been to start very simple, take the correlation of all the simple models and ensemble the ones with the lowest correlation. I also wanted to try voting ensemble, as well as more thorough hyperparameter tuning. A one-man team did not supply me enough time to implement everything. 

---

## Insights from Other Teams

- Two teams used neural networks, and it worked decently well. 

- Another team used balanced tree and bagging models, which they ensembled. This worked really well and I thought that was another approach I should have tried. 

- For this competition I had not considered the possibility of downsampling, and it turns out that many teams tried both upsampling and downsampling. 

- Another approach was SVMs, which one of the top teams used. They also tuned it well, and was able to 

- One of the teams used only XGBoost and did a thorough tuning of the hyperparameters.

- The amount of missing values in the `smoker_status` attribute of the test dataset bothered me, but one group decided to drop it completely, which I thought was smart.

- Another team used logistic regression and set the threshold at 1%...

- One team used violin plots really well... I should start looking into it. 

- GaussianNB + BernoullliNB was something I had not considered.

- One team trained a model to predict the missing values in the dataset. 

- The same team had a nice tsne visualisation. It was beautiful.

- The same team also used balanced models. 

- Another team considered SMOTE, SMOTE Tomek Link and SMOTE + ENN which apparently worked well for them, combined with XGBoost and hyperparameter tuning. 
