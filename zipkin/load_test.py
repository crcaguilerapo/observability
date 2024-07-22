import requests
import json
import time
import random
import uuid

# Zipkin configuration
zipkin_url = "http://localhost:9411/api/v2/spans"

# Function to create a span
def create_span(trace_id, parent_span_id=None):
    span_id = uuid.uuid4().hex[:16]
    timestamp = int(time.time() * 1000)  # In microseconds
    duration = random.randint(1000, 5000)  # Random duration in microseconds

    span = {
        "traceId": trace_id,
        "id": span_id,
        "name": "test-span",
        "timestamp": timestamp * 1000,  # Convert to microseconds
        "duration": duration * 1000,  # Convert to microseconds
        "localEndpoint": {
            "serviceName": "test-service",
            "ipv4": "127.0.0.1"
        },
        "tags": {
            "http.method": "GET",
            "http.path": "/api/test"
        },
        "parentId": parent_span_id if parent_span_id else None
    }

    return span

# Function to create a trace with multiple spans
def create_trace(spans_per_trace):
    trace_id = uuid.uuid4().hex[:16]
    spans = []
    parent_span_id = None

    for _ in range(spans_per_trace):
        span = create_span(trace_id, parent_span_id)
        spans.append(span)
        parent_span_id = span['id']  # The next span will be a child of the current one

    return spans

# Function to send spans to Zipkin
def send_traces(num_traces, spans_per_trace):
    for _ in range(num_traces):
        trace = create_trace(spans_per_trace)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(zipkin_url, data=json.dumps(trace), headers=headers)

        if response.status_code == 202:
            print("Trace successfully sent to Zipkin")
        else:
            print(f"Error sending trace to Zipkin: {response.status_code} - {response.text}")

# Define the number of traces and spans per trace
num_traces = 100  # Example: 5 traces
spans_per_trace = 10  # Example: 3 spans per trace

# Send the traces to Zipkin
send_traces(num_traces, spans_per_trace)
