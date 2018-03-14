# Use Cases

### First Use Case

Name: Build a Machine Learning Model<br/>
What it does: It takes data as inputs and trains a new model that will be used for prediction<br/>
Inputs: Latitude, Longitude, Load Entering from the water treatment plants<br/>
Outputs: What plant capacity is needed for a particular plant in a particular place for a certain amount of water<br/>
How use other components: Data from the water treatment plant database for Europe
Components:
* Machine Learning package: scikitlearn, statsmodels
* Temperature Database for listed countries -- Weather and climate report based on location info
* Population data/report for listed locations
* Primary database
* Packages to sort and combine databases
* Proper dataframe/data structure for combined data

Work Flow:
1. DataMining: 
   * Look into reports/database that is needed
   * Clear the primary database to just keep columns interested.
2. Data Refining:
   * Decide proper data structure and package(s)
   * Create final combined dataframe
3. Choose machine learning algorithm to explore
   * Feature selection of input data
   * Train Model
   * Test Model
   * Compare and iterate with new features or machine learning methods

### Second Use Case

Name: Predict new treatment plant<br/>
What it does: It takes waste water data from the user, what size streams and what type<br/>
Inputs: User gives waste water data, size, and type<br/>
Outputs: Capacity of new water treatment plant and the most similar plants in the database<br/>
How to use other components: Uses the machine learning model, nearest neighbor function and the user interface<br/>
Components:
* The machine learning model
* Nearest neighbor function
* User interface
* Primary database

Work Flow:
1. The user inputs or what information the user need to collect 
   * Locations (e.g., Longitude, Latitude)
   * Waste water entry load
   * Treatment Type (e.g., Nitrogen removal, Phosphorus removla, fitration)

2. Enter the inputs into the machine learning model

3. The machine learning model outputs
   * Capacity fo the treatment plant
   * Compare the inputs the user provide with the primary database, if there is a similar case in the database, 
Suggest the user to contact the existing plant for more information

### Third Use Case

Name: Data Visualization<br/>
What it does: Visualizes the waste water treatment database<br/>
Inputs: Waste water treatment database<br/>
Outputs: plots<br/>
Components:
* Temperature Database for listed countries -- Weather and climate report based on location info
* Population data/report for listed locations
* Primary database
* Packages to sort and combine databases
* Proper dataframe/data structure for combined data
* basic visual model -- such as bar plot, scatter plot, list, tree, etc.
* Packages to add features. For example: color marker, ranking,etc.
* Methods/packages to add interactive features: Zoom-in/out,label,etc.

Working flow:
1. DataMining: 
   * Look into reports/database that is needed
   * Clear the primary database to just keep columns interested.
2. Data Refining:
   * Decide proper data structure and package(s)
   * Create final combined dataframe
3. Basic visulization
   * Create basic model such as bar plots, hitosgram,tree
   * This will probably provide insight for Machine Learning Model
4. Add features
   * Machine Learning model could probably also helps decide what features to add
5. Interactive feature
   * Decide visulization package to make visualization interactive
   * This could also be part of user interface 
How use other components: Machine Learning Model, user interface as suggested above<br/>

##### Primitive Component: User Interface

* 3 page app from dash that runs locally on browser
   * 1st page - default home page
      * No interactive components except for the links to the other pages
      * Description of the project in markdown
      * Describe the two use cases involved and links
   * 2nd page - data visualization
      * interactive graph or visualization
         * how is this going to be interactive - dash or otherwise
      * dropdown menu for plant/agglomeration size that updates the graph
         * interactive component - update graph
   * 3rd page - machine learning model input
      * Agglomeration size - text input
      * dropdown menu for other features that are yes/no
      * input for average max and min temperature
      * output - what capacity is needed and the closest plant in terms of all the inputs