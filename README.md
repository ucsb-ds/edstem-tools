# edstem-tools


This is repo contains scripts useful for gathering data from Ed Stem posts

## `post-to-csv.py`

This will take the json file downloaded from the `Threads JSON` link on the page such as: https://edstem.org/us/courses/77825/analytics/discussion as input.

The script expects that file to be called `all-posts.json` and be in the same file as the script.

Then, the value of `post_number = 3` can be changed to any post in the file.

Running the script with `python3 post-to-csv.py` will output two files:

* `comments_number_3.json` which is the comments on that post only in json form
* `comments_number_3.csv` which is the commment on that post only in CSV form

The fields are: 

```
"name","email","created_at","text"
```

Future improvements:
* Make the input file and post number be command line parameters rather than being hard coded.