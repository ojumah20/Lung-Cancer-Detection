# Lung Cancer Detection in Computed Tomography (CT) scans using Deep Learning Techniques
Using image preprocessing techniques based on tensorflow to detect cases of lung cancer in CT images


**In 2020, lung cancer caused 18% of cancer-related deaths, the highest among all cancers. Early treatments could boost survival rates by up to 45% by 2030. While current screening methods like X-rays and MRIs are less sensitive or invasive, CT scans have become the primary screening tool.

Non-small cell lung cancer (NSCLC) comprises 85% of lung cancer cases, categorized into adenocarcinoma (40%), squamous-cell carcinoma (25-30%), and large-cell carcinoma (5-10%). Accurate CT scan classification is critical to avoid unnecessary procedures and ensure timely treatment. Thus, a deep learning-based computer-aided detection system is needed to reduce misclassification and improve accuracy.

This project uses the Chest CT-Scan Images (CCSI) Dataset from Kaggle, which includes four categories: large-cell carcinoma, squamous-cell carcinoma, adenocarcinoma, and normal cases. Future research could enhance the deep learning pipeline by integrating multiple datasets.**

# Data Loading and Preprocessing
The dataset consists of 10,000 CT images (127.1 MB) organized into test, train, and validation directories, each containing subfolders for different lung cancer classes and normal cases. The define_paths function compiled file paths and labels, which were encoded categorically with one-hot encoding using Keras's flow_from_dataframe.

Data cleaning included noise removal with a median filter and Otsu threshold segmentation. Augmentation techniques like horizontal and vertical flipping were applied using Keras's ImageDataGenerator. Class balancing was achieved through Keras's compute_class_weight.

# Callback and Early Stopping
The callback dynamically adjusted the learning rate during training based on specific conditions. Initialized with parameters like model, patience, threshold, and epochs, it monitored metrics such as loss and accuracy. If training accuracy did not reach 0.95, the learning rate was adjusted according to training accuracy and validation loss. Early stopping was triggered after three epochs without accuracy improvement (patience). Training could also be halted after 15 epochs with user input 'H' or continued for a specified number of additional epochs.

### Weights Saving
The callback tracked the best-performing weights based on validation loss or training accuracy. If no improvement occurred after a set number of epochs (patience), it could restore the model's best weights.

### Baseline Model Creation
A baseline CNN was built using Keras Sequential API, featuring three convolutional layers with increasing filter sizes and ReLU activation, followed by max-pooling and batch normalization. Two dense layers with 256 neurons utilized ReLU and dropout (45%) for regularization. The final dense layer employed softmax for multi-class classification.

### Transfer Learning Models
Pretrained CNNs, EfficientNetB3 and DenseNet121, were used without their final classification layers (`include_top=False`). Weights from ImageNet were applied to enhance feature recognition. Max pooling and batch normalization were implemented for stability and convergence, while L1 and L2 regularization addressed overfitting.

### Dropout and Output Layer
During training, 45% of neurons in the dense layer were dropped to combat overfitting. The output layer consisted of `class_count` neurons with softmax activation for classification.

### Optimizers and Loss Function
Adamax and Adam optimizers were used, with categorical crossentropy as the loss function across all models.

### Model Training and Prediction
Training involved parameters for early stopping, learning rate adjustment, and batch size (set to 8 after optimization). Training was limited to 20 epochs to balance model convergence and computational efficiency.

### Results Visualization
A `plot_confusion_matrix` function was created to visualize model predictions, with Keras's `predict_generator` used to calculate precision, recall, F1-score, and accuracy.

### Fine Tuning
Model performance was assessed with and without image segmentation, comparing ReLU and Leaky ReLU activations and evaluating Adamax and Adam optimizers. The effects of denoising were also analyzed.

### Weights Saving for Selected Deep Learning Pipeline
After training, the best-performing model's weights were saved in H5 format for future reuse in Keras, facilitating transfer learning on additional lung cancer CT images.

Project Diagram
https://github.com/ojumah20/Lung-Cancer-Detection/blob/main/Image%2016-07-2024%20at%2018.11.jpeg
