%define install_base /usr/lib/maddash
%define relnum 0.1.rc1

Name:           maddash
Version:        2.0.2
Release:        %{relnum}%{?dist}
Summary:        MaDDash  
License:        distributable, see LICENSE
Group:          Development/Libraries
URL:            http://code.google.com/p/esnet-perfsonar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       maddash-server
Requires:       maddash-webui
Requires:       nagios-plugins-perfsonar
Requires:       perfsonar-graphs >= 4.0

%description
MaDDash is a framework for scheduling service checks and displaying results in a grid. This package installs a default set of modules that can be used to perform basic maddash functions. 

%pre

%prep

%clean
rm -rf %{buildroot}

%build

%install
mkdir -p %{buildroot}/%{install_base}/
echo "%{version}-%{release}" >  %{buildroot}/%{install_base}/VERSION

%post

%files
%{install_base}/VERSION

