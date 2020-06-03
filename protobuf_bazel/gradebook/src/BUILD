# _____ import build rules for c++ and proto _____
## rules_cc: generate c++ from protobuf
## rules_proto: build protobuf
load("@rules_cc//cc:defs.bzl", "cc_library")
load("@rules_cc//cc:defs.bzl", "cc_binary")
load("@rules_proto//proto:defs.bzl", "proto_library")

# _____ build cpp binary files from cpp _____
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [":gradebook_cc_proto"],
)

# _____ build cpp from proto _____
cc_proto_library(
  name = "gradebook_cc_proto",
  deps = [":gradebook_proto"],
)

# _____ build proto from proto _____
## convention: one rule per proto file
## convention: leave colon in name for rule labels

proto_library(
  name = "gradebook_proto",
  srcs = ["gradebook.proto"],
  deps = [":student_proto" ],
)

proto_library(
  name = "student_proto",
  srcs = ["student.proto"],
  deps = [":grade_proto"],
)

proto_library(
  name = "grade_proto",
  srcs = ["grade.proto"],
)
