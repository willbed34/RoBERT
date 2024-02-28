import csv

# Output lists

def get_csv_data(input_csv_path):
  tweets = []
  labels = []
  # Read the CSV file and extract data
  with open(input_csv_path, 'r', encoding='utf-8') as csv_file:
      csv_reader = csv.reader(csv_file)
      for row in csv_reader:
          #the first column is the label and the last column is the tweet
          label = row[0]
          tweet = row[-1]
          if label == '4':
            labels.append(1)
          else:
            labels.append(0)
          tweets.append(tweet)
  return tweets, labels

def number_to_label(number):
  labels = ['Negative', 'Positive']
  return labels[number]

