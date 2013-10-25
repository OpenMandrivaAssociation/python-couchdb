%define srcname CouchDB
Name:           python-couchdb
Version:        0.9
Release:        1
Summary:        A Python library for working with CouchDB

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/couchdb-python/
Source0:        http://pypi.python.org/packages/source/C/CouchDB/CouchDB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-simplejson
# remove in 2013 once 2010.0 is not supported anymore
Obsoletes:       %{name}-devel < 0.8

%description
Providing a convenient high level interface for the CouchDB server.


%prep
%setup -q -n %{srcname}-%{version}

%build
python setup.py build


%install
python setup.py install --skip-build --root %{buildroot}

# calm rpmlint down
find  %{buildroot}/%{py_puresitedir}/couchdb -name \*.py -print0 | xargs --null chmod 0644


%clean

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt COPYING README.txt 
%doc doc/
%{_bindir}/couchdb-dump
%{_bindir}/couchdb-load
%{_bindir}/couchdb-replicate
%{_bindir}/couchpy
%{py_puresitedir}/CouchDB-%{version}-py%{py_ver}.egg-info
%{py_puresitedir}/couchdb

