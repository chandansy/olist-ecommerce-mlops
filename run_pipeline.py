from pipeline import training_pipeline



if __name__ == '__main__':
    # Run the pipeline
    training_pipeline(data_path='gs://zenml_quickstart/datasets/iris.csv')