#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-Bootstrap
Version  : 2.5.0.0
Release  : 28
URL      : https://files.pythonhosted.org/packages/d5/3e/01858ce3e6988ee2d41f72d7413a83d525dd838803f59e8191e243884403/XStatic-Angular-Bootstrap-2.5.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/3e/01858ce3e6988ee2d41f72d7413a83d525dd838803f59e8191e243884403/XStatic-Angular-Bootstrap-2.5.0.0.tar.gz
Summary  : Angular-Bootstrap 2.5.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-Bootstrap-python = %{version}-%{release}
Requires: XStatic-Angular-Bootstrap-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
-------------------------
        
        Angular-Bootstrap JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.
        
        
        Maintenance
        -----------
        
        To release this package you must use the xstatic-release tool.

%package python
Summary: python components for the XStatic-Angular-Bootstrap package.
Group: Default
Requires: XStatic-Angular-Bootstrap-python3 = %{version}-%{release}
Provides: xstatic-angular-bootstrap-python

%description python
python components for the XStatic-Angular-Bootstrap package.


%package python3
Summary: python3 components for the XStatic-Angular-Bootstrap package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_angular_bootstrap)

%description python3
python3 components for the XStatic-Angular-Bootstrap package.


%prep
%setup -q -n XStatic-Angular-Bootstrap-2.5.0.0
cd %{_builddir}/XStatic-Angular-Bootstrap-2.5.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587079841
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
