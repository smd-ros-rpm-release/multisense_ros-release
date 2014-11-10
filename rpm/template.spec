Name:           ros-hydro-multisense-cal-check
Version:        3.3.6
Release:        0%{?dist}
Summary:        ROS multisense_cal_check package

Group:          Development/Libraries
License:        BSD
URL:            https://bitbucket.org/crl/multisense_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-multisense-ros
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-multisense-ros

%description
multisense_cal_check

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
* Mon Nov 10 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.6-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.5-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.4-0
- Autogenerated by Bloom

* Fri Oct 24 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.3-0
- Autogenerated by Bloom

* Thu Oct 23 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.2-0
- Autogenerated by Bloom

* Thu Oct 09 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.1-0
- Autogenerated by Bloom

* Tue Sep 30 2014 Carnegie Robotics <support@carnegierobotics.com> - 3.3.0-0
- Autogenerated by Bloom

