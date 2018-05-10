Name: wrk
Version: 4.1.0
Release: 1%{?dist}
Summary: HTTP benchmarking tool
License: Modified Apache 2.0 License
URL: https://github.com/wg/wrk

Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

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
make

%install
%{__install} -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE NOTICE
%doc README.md CHANGES SCRIPTING scripts
%{_bindir}/%{name}

%changelog
* Thu May 10 2018 GetPageSpeed Builder <info@getpagespeed.com> 4.1.0-1
- new upstream release 4.1.0
- removed build requires as they are bundled with source now

* Sat Apr 01 2017 GetPageSpeed Builder <info@getpagespeed.com> 4.0.2-2
- new package built with tito

* Mon Nov  7 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 4.0.2-1
- initial release

