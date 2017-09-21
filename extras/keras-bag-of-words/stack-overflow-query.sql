# This query will get 2000 SO posts for the top 20 tags to be fed into our Keras model 
# Here we're only selecting posts with a single tag to keep things simple
# The regex preprocesses the text (strips newlines, commas, and <p> tags), this makes it easier for our model to interpret the text
# We're using partitioning to control the number of posts we get for each tag
# Run this in BigQuery here: https://bigquery.cloud.google.com/savedquery/513927984416:c494494324be4a80b1fc55f613abb39c

SELECT post, tags FROM (
  SELECT 
    TRIM(LOWER(REGEXP_REPLACE(CONCAT(title, ' ', body), r'["\n\'?,]|<p>|</p>'," "))) as post,
    tags,
    row_number() over(partition by tags) row_num
  FROM `bigquery-public-data.stackoverflow.posts_questions` a
  WHERE tags IN ("javascript", "java", "c#", "php", "android", "jquery", "python", "html", "c++", "ios", "css", "mysql", "sql", "asp.net", "ruby-on-rails", "objective-c", "c", ".net", "angularjs", "iphone")
)
WHERE row_num <= 2000
ORDER BY RAND()