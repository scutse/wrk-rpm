Name: wrk
Version: 4.1.0
Release: 1%{?dist}
Summary: a HTTP benchmarking tool
License: Modified Apache 2.0 License
URL: https://github.com/wg/wrk/
Source0: https://github.com/wg/wrk/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
make WITH_LUAJIT=%{_prefix} WITH_OPENSSL=%{_prefix} VER=%{version}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0755 %{name} %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE NOTICE SCRIPTING scripts
%{_bindir}/wrk

%changelog
* Sun Feb 11 2018 GetPageSpeed Builder <info@getpagespeed.com> 4.1.0-1
- 4.1.0

* Sat Apr 01 2017 GetPageSpeed Builder <info@getpagespeed.com> 4.0.2-2
- new package built with tito

* Mon Nov  7 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 4.0.2-1
- initial release

