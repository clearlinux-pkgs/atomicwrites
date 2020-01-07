#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : atomicwrites
Version  : 1.3.0
Release  : 27
URL      : https://files.pythonhosted.org/packages/ec/0f/cd484ac8820fed363b374af30049adc8fd13065720fd4f4c6be8a2309da7/atomicwrites-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/0f/cd484ac8820fed363b374af30049adc8fd13065720fd4f4c6be8a2309da7/atomicwrites-1.3.0.tar.gz
Summary  : Atomic file writes.
Group    : Development/Tools
License  : MIT
Requires: atomicwrites-license = %{version}-%{release}
Requires: atomicwrites-python = %{version}-%{release}
Requires: atomicwrites-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===================
python-atomicwrites
===================
.. image:: https://travis-ci.org/untitaker/python-atomicwrites.svg?branch=master
:target: https://travis-ci.org/untitaker/python-atomicwrites

%package license
Summary: license components for the atomicwrites package.
Group: Default

%description license
license components for the atomicwrites package.


%package python
Summary: python components for the atomicwrites package.
Group: Default
Requires: atomicwrites-python3 = %{version}-%{release}

%description python
python components for the atomicwrites package.


%package python3
Summary: python3 components for the atomicwrites package.
Group: Default
Requires: python3-core

%description python3
python3 components for the atomicwrites package.


%prep
%setup -q -n atomicwrites-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549029199
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/atomicwrites
cp LICENSE %{buildroot}/usr/share/package-licenses/atomicwrites/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/atomicwrites/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
