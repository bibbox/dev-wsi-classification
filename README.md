# WSI Classification Test fro Whole Slide Images


 ## Setup and Install
 - Python 3.5 & above required!
 - clone the project 
   > git clone  https://github.com/bibbox/dev-wsi-classification
    
 - Create virtual environment, if you want using virtualenv command
 - Install dependent libararies
   > pip install -r requirements.txt
    
 ## Organise the train folder
 - Run data processing python code to re-arrange folders by label
 - Script is "Hardwired" to work with the PV_SS data set (contact Markus)
 - Structure of Testimages is described in 
     - typeTable.csv
     - slideTable.csv
     - slideScanMap.csv
     - scanTable.csv
   > python data_processing.py 
   
 ## Train your model using our processed dataset
 - Run the below command to train your model using CNN architectures. 
 - change the  --image_dir parameter
 - By default, below script will download 'Google's inception architecture - 'inception-2015-12-05.tgz'.
 
   > python retrain.py --image_dir=/Users/Shared/SWD/TENSORFLOW-EXPERIMENTS/PV_SS/TRAINING -bottleneck_dir=bottleneck/ --how_many_training_steps=1500 --output_graph=trained_model/retrained_graph.pb --output_labels=trained_model/retrained_labels.txt --summaries_dir=summaries
  
  
  ## Test your model
  - Run the below python script to classify your test images based on our pre-trained model.
    > python classify.py        
          
 ## TODOS
  - make the generation of the training / test data sets parameterized
  - make the evaluation of the trained model parameterized
  - add diagrams for the evaluation
 
  
  
 
