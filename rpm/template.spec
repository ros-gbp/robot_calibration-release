%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-robot-calibration
Version:        0.6.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS robot_calibration package

License:        Apache2
URL:            http://ros.org/wiki/robot_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ceres-solver-devel
Requires:       gflags-devel
Requires:       orocos-kdl-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-camera-calibration-parsers
Requires:       ros-noetic-control-msgs
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-moveit-msgs
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-robot-calibration-msgs
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-visualization-msgs
Requires:       suitesparse-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  gflags-devel
BuildRequires:  orocos-kdl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-camera-calibration-parsers
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-code-coverage
BuildRequires:  ros-noetic-control-msgs
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-moveit-msgs
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-robot-calibration-msgs
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-visualization-msgs
BuildRequires:  suitesparse-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Calibrate a Robot

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Nov 02 2020 Michael Ferguson <mike@vanadiumlabs.com> - 0.6.4-1
- Autogenerated by Bloom

