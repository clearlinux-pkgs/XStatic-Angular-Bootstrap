#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-Bootstrap
Version  : 2.2.0.0
Release  : 18
URL      : http://pypi.debian.net/XStatic-Angular-Bootstrap/XStatic-Angular-Bootstrap-2.2.0.0.tar.gz
Source0  : http://pypi.debian.net/XStatic-Angular-Bootstrap/XStatic-Angular-Bootstrap-2.2.0.0.tar.gz
Summary  : Angular-Bootstrap 2.2.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-Bootstrap-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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
Provides: xstatic-angular-bootstrap-python

%description python
python components for the XStatic-Angular-Bootstrap package.


%prep
%setup -q -n XStatic-Angular-Bootstrap-2.2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503087518
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503087518
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
