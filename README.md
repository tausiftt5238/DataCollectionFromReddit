This is to automate the process of collecting data for:
1. [Reddit Comments](https://files.pushshift.io/reddit/comments/)
2. [Reddit Submissions](https://files.pushshift.io/reddit/submissions/)

So far, there are 3 types of compressed files that can be found in the pushshift website.
3 types of those files are dealt with eventually.
1. zst
2. bz2
3. xz

For now, to download any specific type of compressed file, 
we use the following command:

1. For zst files:
`python deal_with_zst.py URL`
2. for bz2 files:
`python deal_with_bz2.py URL`