from jina import Flow

f = (
    Flow(protocol="HTTP", port=5001)
    .add(name="foo", uses="docker://jina-tryout-foo", )
    .add(name="bar", uses="docker://jina-tryout-bar", uses_after="foo")
)

f.to_docker_compose_yaml("docker-compose.yml")