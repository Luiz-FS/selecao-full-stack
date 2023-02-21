#!/bin/sh
cd realtimequote
export $(grep -v '^#' .env_test | xargs)
pytest