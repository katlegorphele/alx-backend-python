from client import GithubOrgClient

# Create a GithubOrgClient instance for the "google" organization
client = GithubOrgClient("google")

# Get a list of public repositories for the organization
repos = client.public_repos()

# Print the names of the repositories
for repo in repos:
    print(repo)

