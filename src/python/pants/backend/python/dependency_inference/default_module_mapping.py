# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# NB: The project names must follow the naming scheme at
#  https://www.python.org/dev/peps/pep-0503/#normalized-names.
DEFAULT_MODULE_MAPPING = {
    "absl-py": ("absl",),
    "acryl-datahub": ("datahub",),
    "ansicolors": ("colors",),
    "apache-airflow": ("airflow",),
    "atlassian-python-api": ("atlassian",),
    "attrs": ("attr", "attrs"),
    # Azure
    "azure-common": ("azure.common",),
    "azure-core": ("azure.core",),
    "azure-cosmos": ("azure.cosmos",),
    "azure-graphrbac": ("azure.graphrbac",),
    "azure-identity": ("azure.identity",),
    "azure-keyvault-certificates": ("azure.keyvault.certificates",),
    "azure-keyvault-keys": ("azure.keyvault.keys",),
    "azure-keyvault-secrets": ("azure.keyvault.secrets",),
    "azure-keyvault": ("azure.keyvault",),
    "azure-mgmt-apimanagement": ("azure.mgmt.apimanagement",),
    "azure-mgmt-authorization": ("azure.mgmt.authorization",),
    "azure-mgmt-automation": ("azure.mgmt.automation",),
    "azure-mgmt-batch": ("azure.mgmt.batch",),
    "azure-mgmt-compute": ("azure.mgmt.compute",),
    "azure-mgmt-consumption": ("azure.mgmt.consumption",),
    "azure-mgmt-containerinstance": ("azure.mgmt.containerinstance",),
    "azure-mgmt-containerregistry": ("azure.mgmt.containerregistry",),
    "azure-mgmt-containerservice": ("azure.mgmt.containerservice",),
    "azure-mgmt-core": ("azure.mgmt.core",),
    "azure-mgmt-cosmosdb": ("azure.mgmt.cosmosdb",),
    "azure-mgmt-dns": ("azure.mgmt.dns",),
    "azure-mgmt-eventgrid": ("azure.mgmt.eventgrid",),
    "azure-mgmt-eventhub": ("azure.mgmt.eventhub",),
    "azure-mgmt-frontdoor": ("azure.mgmt.frontdoor",),
    "azure-mgmt-hybridkubernetes": ("azure.mgmt.hybridkubernetes",),
    "azure-mgmt-iothub": ("azure.mgmt.iothub",),
    "azure-mgmt-iothubprovisioningservices": ("azure.mgmt.iothubprovisioningservices",),
    "azure-mgmt-keyvault": ("azure.mgmt.keyvault",),
    "azure-mgmt-logic": ("azure.mgmt.logic",),
    "azure-mgmt-managementgroups": ("azure.mgmt.managementgroups",),
    "azure-mgmt-monitor": ("azure.mgmt.monitor",),
    "azure-mgmt-msi": ("azure.mgmt.msi",),
    "azure-mgmt-network": ("azure.mgmt.network",),
    "azure-mgmt-privatedns": ("azure.mgmt.privatedns",),
    "azure-mgmt-rdbms": ("azure.mgmt.rdbms",),
    "azure-mgmt-redis": ("azure.mgmt.redis",),
    "azure-mgmt-resource": ("azure.mgmt.resource",),
    "azure-mgmt-resourcegraph": ("azure.mgmt.resourcegraph",),
    "azure-mgmt-security": ("azure.mgmt.security",),
    "azure-mgmt-servicebus": ("azure.mgmt.servicebus",),
    "azure-mgmt-servicefabric": ("azure.mgmt.servicefabric",),
    "azure-mgmt-sql": ("azure.mgmt.sql",),
    "azure-mgmt-storage": ("azure.mgmt.storage",),
    "azure-mgmt-subscription": ("azure.mgmt.subscription",),
    "azure-mgmt-synapse": ("azure.mgmt.synapse",),
    "azure-mgmt-trafficmanager": ("azure.mgmt.trafficmanager",),
    "azure-mgmt-web": ("azure.mgmt.web",),
    "azure-eventgrid": ("azure.eventgrid",),
    "azure-eventhub": ("azure.eventhub",),
    "azure-servicebus": ("azure.servicebus",),
    "azure-storage-blob": ("azure.storage.blob",),
    "azure-storage-queue": ("azure.storage.queue",),
    "azure-synapse-accesscontrol": ("azure.synapse.accesscontrol",),
    "beautifulsoup4": ("bs4",),
    "bitvector": ("BitVector",),
    "cattrs": ("cattr",),
    "django-admin-cursor-paginator": ("admin_cursor_paginator",),
    "django-cors-headers": ("corsheaders",),
    "django-csp": ("csp",),
    "django-debug-toolbar": ("debug_toolbar",),
    "django-dotenv": ("dotenv",),
    "django-filter": ("django_filters",),
    "django-import-export": ("import_export",),
    "django-ipware": ("ipware",),
    "django-model-utils": ("model_utils",),
    "django-ninja": ("ninja",),
    "django-ninja-extra": ("ninja_extra",),
    "django-postgres-extra": ("psqlextra",),
    "django-safedelete": ("safedelete",),
    "django-simple-history": ("simple_history",),
    "django-storages": ("storages",),
    "django-taggit": ("taggit",),
    "django-taggit-autosuggest": ("taggit_autosuggest",),
    "djangorestframework": ("rest_framework",),
    "djangorestframework-dataclasses": ("rest_framework_dataclasses",),
    "djangorestframework-simplejwt": ("rest_framework_simplejwt",),
    "elastic-apm": ("elasticapm",),
    "enum34": ("enum",),
    "factory-boy": ("factory",),
    "fluent-logger": ("fluent",),
    "gitpython": ("git",),
    # See https://github.com/googleapis/google-cloud-python#libraries for all Google cloud
    # libraries. We only add libraries in GA, not beta.
    "google-cloud-aiplatform": ("google.cloud.aiplatform",),
    "google-cloud-bigquery": ("google.cloud.bigquery",),
    "google-cloud-bigtable": ("google.cloud.bigtable",),
    "google-cloud-datastore": ("google.cloud.datastore",),
    "google-cloud-datastream": ("google.cloud.datastream",),
    "google-cloud-firestore": ("google.cloud.firestore",),
    "google-cloud-functions": ("google.cloud.functions_v1", "google.cloud.functions"),
    "google-cloud-iam": ("google.cloud.iam_credentials_v1",),
    "google-cloud-iot": ("google.cloud.iot_v1",),
    "google-cloud-logging": ("google.cloud.logging_v2", "google.cloud.logging"),
    "google-cloud-pubsub": ("google.cloud.pubsub_v1", "google.cloud.pubsub"),
    "google-cloud-secret-manager": ("google.cloud.secretmanager",),
    "google-cloud-spanner": ("google.cloud.spanner",),
    "google-cloud-storage": ("google.cloud.storage",),
    "graphql-core": ("graphql",),
    "grpcio": ("grpc",),
    "ipython": ("IPython",),
    "jack-client": ("jack",),
    "kafka-python": ("kafka",),
    "lark-parser": ("lark",),
    "launchdarkly-server-sdk": ("ldclient",),
    "mail-parser": ("mailparser",),
    "mysql-connector-python": ("mysql.connector",),
    "opencv-python": ("cv2",),
    "opensearch-py": ("opensearchpy",),
    # opentelemetry
    "opentelemetry-api": ("opentelemetry",),
    "opentelemetry-exporter-otlp": ("opentelemetry.exporter",),
    "opentelemetry-exporter-otlp-proto-grpc": ("opentelemetry.exporter.otlp.proto.grpc",),
    "opentelemetry-exporter-otlp-proto-http": ("opentelemetry.exporter.otlp.proto.http",),
    "opentelemetry-instrumentation-aio-pika": ("opentelemetry.instrumentation.aio_pika",),
    "opentelemetry-instrumentation-aiohttp-client": (
        "opentelemetry.instrumentation.aiohttp_client",
    ),
    "opentelemetry-instrumentation-aiopg": ("opentelemetry.instrumentation.aiopg",),
    "opentelemetry-instrumentation-asgi": ("opentelemetry.instrumentation.asgi",),
    "opentelemetry-instrumentation-asyncpg": ("opentelemetry.instrumentation.asyncpg",),
    "opentelemetry-instrumentation-aws-lambda": ("opentelemetry.instrumentation.aws_lambda",),
    "opentelemetry-instrumentation-boto": ("opentelemetry.instrumentation.boto",),
    "opentelemetry-instrumentation-boto3sqs": ("opentelemetry.instrumentation.boto3sqs",),
    "opentelemetry-instrumentation-botocore": ("opentelemetry.instrumentation.botocore",),
    "opentelemetry-instrumentation-celery": ("opentelemetry.instrumentation.celery",),
    "opentelemetry-instrumentation-confluent-kafka": (
        "opentelemetry.instrumentation.confluent_kafka",
    ),
    "opentelemetry-instrumentation-dbapi": ("opentelemetry.instrumentation.dbapi",),
    "opentelemetry-instrumentation-django": ("opentelemetry.instrumentation.django",),
    "opentelemetry-instrumentation-elasticsearch": ("opentelemetry.instrumentation.elasticsearch",),
    "opentelemetry-instrumentation-falcon": ("opentelemetry.instrumentation.falcon",),
    "opentelemetry-instrumentation-fastapi": ("opentelemetry.instrumentation.fastapi",),
    "opentelemetry-instrumentation-flask": ("opentelemetry.instrumentation.flask",),
    "opentelemetry-instrumentation-grpc": ("opentelemetry.instrumentation.grpc",),
    "opentelemetry-instrumentation-httpx": ("opentelemetry.instrumentation.httpx",),
    "opentelemetry-instrumentation-jinja2": ("opentelemetry.instrumentation.jinja2",),
    "opentelemetry-instrumentation-kafka-python": ("opentelemetry.instrumentation.kafka",),
    "opentelemetry-instrumentation-logging": ("opentelemetry.instrumentation.logging",),
    "opentelemetry-instrumentation-mysql": ("opentelemetry.instrumentation.mysql",),
    "opentelemetry-instrumentation-pika": ("opentelemetry.instrumentation.pika",),
    "opentelemetry-instrumentation-psycopg2": ("opentelemetry.instrumentation.psycopg2",),
    "opentelemetry-instrumentation-pymemcache": ("opentelemetry.instrumentation.pymemcache",),
    "opentelemetry-instrumentation-pymongo": ("opentelemetry.instrumentation.pymongo",),
    "opentelemetry-instrumentation-pymysql": ("opentelemetry.instrumentation.pymysql",),
    "opentelemetry-instrumentation-pyramid": ("opentelemetry.instrumentation.pyramid",),
    "opentelemetry-instrumentation-redis": ("opentelemetry.instrumentation.redis",),
    "opentelemetry-instrumentation-remoulade": ("opentelemetry.instrumentation.remoulade",),
    "opentelemetry-instrumentation-requests": ("opentelemetry.instrumentation.requests",),
    "opentelemetry-instrumentation-sklearn": ("opentelemetry.instrumentation.sklearn",),
    "opentelemetry-instrumentation-sqlalchemy": ("opentelemetry.instrumentation.sqlalchemy",),
    "opentelemetry-instrumentation-sqlite3": ("opentelemetry.instrumentation.sqlite3",),
    "opentelemetry-instrumentation-starlette": ("opentelemetry.instrumentation.starlette",),
    "opentelemetry-instrumentation-system-metrics": (
        "opentelemetry.instrumentation.system_metrics",
    ),
    "opentelemetry-instrumentation-tornado": ("opentelemetry.instrumentation.tornado",),
    "opentelemetry-instrumentation-tortoiseorm": ("opentelemetry.instrumentation.tortoiseorm",),
    "opentelemetry-instrumentation-urllib": ("opentelemetry.instrumentation.urllib",),
    "opentelemetry-instrumentation-urllib3": ("opentelemetry.instrumentation.urllib3",),
    "opentelemetry-instrumentation-wsgi": ("opentelemetry.instrumentation.wsgi",),
    "opentelemetry-sdk": ("opentelemetry.sdk",),
    "opentelemetry-test-utils": ("opentelemetry.test",),
    "oslo-cache": ("oslo_cache",),
    "oslo-concurrency": ("oslo_concurrency",),
    "oslo-config": ("oslo_config",),
    "oslo-context": ("oslo_context",),
    "oslo-db": ("oslo_db",),
    "oslo-i18n": ("oslo_i18n",),
    "oslo-limit": ("oslo_limit",),
    "oslo-log": ("oslo_log",),
    "oslo-messaging": ("oslo_messaging",),
    "oslo-metrics": ("oslo_metrics",),
    "oslo-middleware": ("oslo_middleware",),
    "oslo-policy": ("oslo_policy",),
    "oslo-privsep": ("oslo_privsep",),
    "oslo-reports": ("oslo_reports",),
    "oslo-rootwrap": ("oslo_rootwrap",),
    "oslo-serialization": ("oslo_serialization",),
    "oslo-service": ("oslo_service",),
    "oslo-upgradecheck": ("oslo_upgradecheck",),
    "oslo-utils": ("oslo_utils",),
    "oslo-versionedobjects": ("oslo_versionedobjects",),
    "oslo-vmware": ("oslo_vmware",),
    "paho-mqtt": ("paho",),
    "phonenumberslite": ("phonenumbers",),
    "pillow": ("PIL",),
    "pip-tools": ("piptools",),
    "progressbar2": ("progressbar",),
    "protobuf": ("google.protobuf",),
    "psycopg2-binary": ("psycopg2",),
    "pycrypto": ("Crypto",),
    "pykube-ng": ("pykube",),
    "pyhamcrest": ("hamcrest",),
    "pygithub": ("github",),
    "pygobject": ("gi",),
    "pyjwt": ("jwt",),
    "pyopenssl": ("OpenSSL",),
    "pypdf2": ("PyPDF2",),
    "pypi-kenlm": ("kenlm",),
    "pysocks": ("socks",),
    "pytest": ("pytest", "_pytest"),
    "python-dateutil": ("dateutil",),
    "python-docx": ("docx",),
    "python-dotenv": ("dotenv",),
    "python-editor": ("editor",),
    "python-engineio": ("engineio",),
    "python-hcl2": ("hcl2",),
    "python-jose": ("jose",),
    "python-json-logger": ("pythonjsonlogger",),
    "python-levenshtein": ("Levenshtein",),
    "python-lsp-jsonrpc": ("pylsp_jsonrpc",),
    "python-magic": ("magic",),
    "python-pptx": ("pptx",),
    "python-slugify": ("slugify",),
    "python-socketio": ("socketio",),
    "python-statsd": ("statsd",),
    "pyyaml": ("yaml",),
    "pymongo": ("bson", "gridfs", "pymongo"),
    "pymupdf": ("fitz",),
    "pytest-runner": ("ptr",),
    "pywinrm": ("winrm",),
    "randomwords": ("random_words",),
    "scikit-image": ("skimage",),
    "scikit-learn": ("sklearn",),
    "scikit-video": ("skvideo",),
    "sseclient-py": ("sseclient",),
    "setuptools": ("easy_install", "pkg_resources", "setuptools"),
    "snowflake-connector-python": ("snowflake.connector",),
    "snowflake-snowpark-python": ("snowflake.snowpark",),
    "snowflake-sqlalchemy": ("snowflake.sqlalchemy",),
    "strawberry-graphql": ("strawberry",),
    "streamlit-aggrid": ("st_aggrid",),
    "unleashclient": ("UnleashClient",),
    "websocket-client": ("websocket",),
}

DEFAULT_TYPE_STUB_MODULE_MAPPING = {
    "djangorestframework-types": ("rest_framework",),
    "lark-stubs": ("lark",),
    "types-beautifulsoup4": ("bs4",),
    "types-enum34": ("enum34",),
    "types-pillow": ("PIL",),
    "types-protobuf": ("google.protobuf",),
    "types-pycrypto": ("Crypto",),
    "types-pyopenssl": ("OpenSSL",),
    "types-pyyaml": ("yaml",),
    "types-python-dateutil": ("dateutil",),
    "types-setuptools": ("easy_install", "pkg_resources", "setuptools"),
}
