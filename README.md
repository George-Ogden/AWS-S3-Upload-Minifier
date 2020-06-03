# HTML, CSS and JS Minifier
Python 3.8 lambda function to compress the main files in your website.
The function is designed to run on a create event trigger.
The function also deletes the file extension of .html to give a more professional feel to a website.

## Necessary permissions
In order to modify files, a policy is needed for the lambda function (or you can add AmazonS3FullAccess if you are lazy):
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::responsiveandready"
            ]
        }
    ]
}
```

## Handler Configuration
Handler property should be configured to `minifier.handler` and an event should be set up in S3 to invoke this function on uploads.

All dependencies are installed in the zip folder so it can just be uploaded.

## Thank you
Thank you to [@chilts](https://github.com/chilts), who has written the API.