Name:           ros-hydro-multisense-ros
Version:        3.3.1
Release:        0%{?dist}
Summary:        ROS multisense_ros package

Group:          Development/Libraries
License:        BSD
URL:            https://bitbucket.org/crl/multisense_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-angles
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-genmsg
Requires:       ros-hydro-image-geometry
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-multisense-lib
Requires:       ros-hydro-opencv2
Requires:       ros-hydro-rosbag
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-genmsg
BuildRequires:  ros-hydro-image-geometry
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-message-runtime
BuildRequires:  ros-hydro-multisense-lib
BuildRequires:  ros-hydro-opencv2
BuildRequires:  ros-hydro-rosbag
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  yaml-cpp-devel

%description
multisense_ros

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Oct 09 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.1-0
- Autogenerated by Bloom

* Tue Sep 30 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.0-0
- Autogenerated by Bloom

