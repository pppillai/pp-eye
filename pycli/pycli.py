import click
import requests
import os

ERROR_COLOR="red"
SUCCESS_COLOR="green"

@click.command()
@click.argument('name', required=False)
def greet(name):

    # hardcoded environment variables
    cluster_ip = os.environ.get("KUBECLUSTERIP")
    cluster_port = os.environ.get("NODEPORTPORT")

    if cluster_ip is None:
        click.secho("KUBERCLUSTERIP environment variable not set",
        fg=ERROR_COLOR, bold=True)
        return 1
    if cluster_port is None:
        click.secho("NODEPORTPORT environment varibale not set",
        fg=ERROR_COLOR, bold=True)
        return 1
    
    if name is not None:
        url = f"http://{cluster_ip}:{cluster_port}/{name}"
    else:
        url = f"http://{cluster_ip}:{cluster_port}"

    # do the call    
    try:
        resp = requests.get(url)
        click.secho(resp.text, fg=SUCCESS_COLOR, bold=False)
    except Exception:
        click.secho(Exception, fg=ERROR_COLOR, bold=True)

    return 0