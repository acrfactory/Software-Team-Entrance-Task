// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Completed.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__COMPLETED__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__COMPLETED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/completed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Completed_heading
{
public:
  explicit Init_Completed_heading(::interfaces::msg::Completed & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Completed heading(::interfaces::msg::Completed::_heading_type arg)
  {
    msg_.heading = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Completed msg_;
};

class Init_Completed_distance
{
public:
  explicit Init_Completed_distance(::interfaces::msg::Completed & msg)
  : msg_(msg)
  {}
  Init_Completed_heading distance(::interfaces::msg::Completed::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_Completed_heading(msg_);
  }

private:
  ::interfaces::msg::Completed msg_;
};

class Init_Completed_longitude
{
public:
  explicit Init_Completed_longitude(::interfaces::msg::Completed & msg)
  : msg_(msg)
  {}
  Init_Completed_distance longitude(::interfaces::msg::Completed::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_Completed_distance(msg_);
  }

private:
  ::interfaces::msg::Completed msg_;
};

class Init_Completed_latitude
{
public:
  Init_Completed_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Completed_longitude latitude(::interfaces::msg::Completed::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_Completed_longitude(msg_);
  }

private:
  ::interfaces::msg::Completed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Completed>()
{
  return interfaces::msg::builder::Init_Completed_latitude();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__COMPLETED__BUILDER_HPP_
