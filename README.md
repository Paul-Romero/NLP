# About the project
In this project I have tried to create a Python software using Natural Language Processing techniques and some Machine Learning. In order to classify the text of an online chat and generate an alert in case it is cyberbullyng or similar. For this, a web page was designed as a test platform for the system.
# Built with
Technologies used to build the software:
* [Anaconda](https://www.anaconda.com/)
* [NLTK](https://www.nltk.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
# Working scheme
The illustration shows in a simple way the process of the whole system.
![system scheme](https://user-images.githubusercontent.com/66179885/139366105-6966186a-8f83-4895-8326-62e07ddfe81d.png)
# Model evaluation
The functions of the scikit-learn library are applied to measure the precision and the other scores of each model created for the classification
|Algorithm | Accuracy | Precision | Sensibility | F1 Score | Mean absolute error |
|----------|----------|-----------|-------------|----------|-------------------- |
|Naive Bayes | 88.29% | 87.69% | 84.74% | 86.19% | 11.71% |
|Support Machine Vector | 88.84% | 90.72% | 82.56% | 86.45% | 11.16% |
|Random Forest | 87.94% | 89.69% | 81.38% | 85.35% |12.06% |
# Screenshots
![main](https://user-images.githubusercontent.com/66179885/139369018-e5a9ed6c-9112-4ad7-972b-27b166d5096e.png)
![chat](https://user-images.githubusercontent.com/66179885/139370027-5b9db580-b912-4eb5-ba9e-973e0808ad4e.png)
# Conclusions
It was possible to design a website as a chat room platform in order to check the operation of the classifier model in an almost real environment, taking as input the messages sent by the users of the room and analyzing them, to later issue an alert that acts as a parental control when the model classifies one of the messages as grooming.
