#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-Bootstrap
Version  : 0.11.0.2
Release  : 9
URL      : https://pypi.python.org/packages/source/X/XStatic-Angular-Bootstrap/XStatic-Angular-Bootstrap-0.11.0.2.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Angular-Bootstrap/XStatic-Angular-Bootstrap-0.11.0.2.tar.gz
Summary  : Angular-Bootstrap 0.11.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-Bootstrap-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Angular-Bootstrap
-------------------------
Angular-Bootstrap JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Angular-Bootstrap package.
Group: Default

%description python
python components for the XStatic-Angular-Bootstrap package.


%prep
%setup -q -n XStatic-Angular-Bootstrap-0.11.0.2

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
