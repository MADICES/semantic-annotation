#!/usr/bin/env bash

set -ex

cat Test_Data/3fe5dguZxs7e7bVbfAdjmHXnCI8u.json |
    jq '{entry_id} + (.archive.data | {
      m_def,
      name,
      datetime,
      location,
      reaction_class,
      reaction_name,
      experimenter,
      data_file,
      samples,
      reactor_filling,
      reaction_results: (.reaction_results) | {
          reactants_conversions: .reactants_conversions[].name
      }
    })'
