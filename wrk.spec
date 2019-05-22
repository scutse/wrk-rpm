Name: wrk
Version: 4.1.0
Release: 1%{?dist}
Summary: HTTP benchmarking tool
License: Modified Apache 2.0 License
URL: https://github.com/wg/wrk

Source0: %{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%if ( 0%{?fedora} >= 27 )
%global debug_package %{nil}
BuildRequires: perl
%endif

%description
  wrk is a modern HTTP benchmarking tool capable of generating significant
  load when run on a single multi-core CPU. It combines a multithreaded
  design with scalable event notification systems such as epoll and kqueue.

  An optional LuaJIT script can perform HTTP request generation, response
  processing, and custom reporting. Details are available in SCRIPTING and
  several examples are located in %{_docdir}/%{name}-%{version}/scripts/

%prep
%setup -q

%build
# EL7 doesn't have this macro: %make_build VER=%{version}
%{__make} VER=%{version} %{?_smp_mflags} 

%install
%{__install} -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
# Virtually add license macro for EL6:
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%doc README.md CHANGES SCRIPTING scripts
%{_bindir}/%{name}

%changelog
