// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/Completed.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__COMPLETED__STRUCT_H_
#define INTERFACES__MSG__DETAIL__COMPLETED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Completed in the package interfaces.
typedef struct interfaces__msg__Completed
{
  double latitude;
  double longitude;
  double distance;
  double heading;
} interfaces__msg__Completed;

// Struct for a sequence of interfaces__msg__Completed.
typedef struct interfaces__msg__Completed__Sequence
{
  interfaces__msg__Completed * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__Completed__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__COMPLETED__STRUCT_H_
