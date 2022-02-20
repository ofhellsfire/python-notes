# Web :: Authentication

There are two large groups or categories of tokens:

1. Random tokens
2. Signed tokens

## Random Tokens

Random tokens are composed of a sequence of random characters.

When you generate a random token for a client, you have to preserve this token in your user database under the user represented by the client. 
This is necessary because later when the client presents the token for authentication you will have to ensure it matches the original.

If you want to have the utmost security, you can encrypt the tokens before you store them in your database.
For this you can use your favorite encryption algorithm, or your database's encryption facilities if available.
If you decide to implement encryption for your tokens, you should make sure you don't store your encryption key(s) in the same database as your encrypted tokens.
If you feel confident that you have good security practices on the server that hosts your database, then encrypting the tokens might be an unnecessary complication.

You will want to have an index built on the database column that holds your tokens (encryption will definitely complicate this!), so that when a client authenticates with a token you can search this index and quickly determine which user owns the token.

## Signed Tokens

Signed token has three components: a header, one or more claims, and the signature.

The header stores metadata about the token that is useful in decoding and verifying the token. This can include cryptographic signing algorithms used, version numbers and similar information that is not sensitive.

Claims describe the client requesting the token. The most common claims for an authentication token are the user ID and the user role, but other claims that make sense for the application can be added.
Claims stored in tokens are not encrypted, so you should avoid storing sensitive information such as passwords or API keys.

The signature part of the token is what provides legitimacy to the claims. This signature is generated from the information contained in the claims using cryptographic functions and a secret key that is only known to the server that generates the tokens. Once a signature is attached to the token, it is not possible to alter the claims, because changes made to the claims would render the signature invalid.

To authenticate a client with a signed token it is necessary to first validate the token signature. If the signature does not validate, then access is denied. If the signature passes validation, then access is granted.

The algorithms used in generating and verifying the signatures can be symmetric or asymmetric. When using symmetric signing algorithms, the same secret key used to sign the token needs to be used when the token signature is verified. Asymmetric signing algorithms use two keys, a secret key to sign the token and a public key to verify it. The benefit of asymmetric signing is that it allows anybody to verify signed tokens, without compromising their security.

The most important difference signed tokens have is that they do not need to be stored in your user database, because the information about the user is stored directly inside the token. So for a signed token, you just have to generate the token and return it to your client. When the token is presented back for authentication, the server just needs to verify the signature and use the claims to identify the user. While not needing to store tokens in a database seems like a great advantage, this has a problem: token revocation.

## Token Revocation

An important security consideration when working with token authentication is making it easy to revoke tokens. This is not only important to control a leak, but also as a "logout" mechanism that clients can use to disable a token once they don't need it anymore, ensuring that even if this discarded token is leaked it won't be of use.

If you are using random tokens, revoking a token requires removing the token from the database. Once the token is not in the database, it won't work as authentication. Typically it can be implemented as an endpoint such as `/tokens` with the `DELETE` method to do the revocation.

If you use signed tokens, then the revocation process is much more difficult, because these tokens are not stored in a central database from where they can be deleted. The solution for this type of token is to build a revoked tokens table in your database, where tokens that are revoked are stored. When a client presents a token for authentication, the revoked token table must be searched and if the token appears in this table, then the request must be denied, even if the token is otherwise valid. If your tokens have an expiration, then they only need to be in the revoked tokens table during the validate period. A background task (maybe a cron job) can run at regular intervals and purge any expired revoked tokens, since once they are expired they do not present a risk anymore.

## How Does the Client Get the Token?

### Copy/Paste Method

An approach that is widely used by API services that are typically called from application servers (as opposite to a browser) is to show the token (sometimes called API key) in the website of the service provider. The developer of the consumer application must copy the token from the provider's website and then add it to their application configuration. If your API is designed to be called by other servers, then this is a good model to use.

### Auth Endpoint Method

When the consumer application runs in the browser the solution described above does not work, first because the browser is an insecure platform where it is not possible to safely store a token or API key, but also because you'll very likely want each user who logs in to the application to use their own individual token.

For this type of application the process is more involved. When the user logs in, for example by providing an email address and a password, the browser sends a request to a token endpoint, authenticating on behalf of the user with the credentials provided. If the endpoint verifies the credentials, then it generates a token for the client and returns it in the response. From then on, the client authenticates their requests with this token. The two-legged OAuth protocol is a well known example of this process.

Authentication for this method is often implemented using the HTTP Basic Authentication standard, in which the client passes the user provided credentials in the Authorization header of the request, with the following structure: `Authorization: Basic base64("<username>:<password>")`

The solution can be made more elaborate by the use of two tokens, an access token and a refresh token. An access token is used for authenticating against API endpoints, but this token is provided with a relatively short expiration time. When the token expires, it cannot be used anymore, and the client must request a new access token by invoking another endpoint that is authenticated with the refresh token.

## Authenticating API Endpoints

Once the client is in possession of a token, it can send authenticated requests. The actual authentication mechanism that is often used is Bearer Authentication, which also uses the Authorization header: `Authorization: Bearer <token>`

Basic and Bearer authentication implementations can coexist in the same application.

*NOTE: Bearer authentication (also called token authentication) is an HTTP authentication scheme that involves security tokens called bearer tokens. The name "Bearer authentication" can be understood as "give access to the bearer of this token". The bearer token is a cryptic string, usually generated by the server in response to a login request.*

Additional resource: https://swagger.io/docs/specification/authentication/bearer-authentication/
