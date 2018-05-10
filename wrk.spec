Name: wrk
Version: 4.0.2
Release: 1%{?dist}
Summary: HTTP benchmarking tool
License: Modified Apache 2.0 License
URL: https://github.com/wg/wrk

Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: openssl-devel
BuildRequires: luajit-devel

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
%make_build VER=%{version}

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir}/%{name} %{name}

%files
%license LICENSE NOTICE
%doc README CHANGES SCRIPTING scripts
%{_bindir}/%{name}

%changelog

* Sat Apr 01 2017 GetPageSpeed Builder <info@getpagespeed.com> 4.0.2-2
- new package built with tito

* Mon Nov  7 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 4.0.2-1
- initial release

