%define srcname CouchDB
Name:           python-couchdb
Version:        1.2
Release:        1
Summary:        A Python library for working with CouchDB

Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/couchdb-python/
Source0:        http://pypi.python.org/packages/source/C/CouchDB/CouchDB-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgcinfig(python)
BuildRequires:  pkgcinfig(python2)
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools
Requires:       python3dist(simplejson)
Requires:       python2dist(simplejson)
# remove in 2013 once 2010.0 is not supported anymore
Obsoletes:       %{name}-devel < 0.8

%description
Providing a convenient high level interface for the CouchDB server.

%package -n python2-couchdb
Summary:	Providing a convenient high level interface for the CouchDB server.

Group:		Development/Python
 
%description -n python2-couchdb
Providing a convenient high level interface for the CouchDB server.


%prep
%setup -q -n %{srcname}-%{version}

mv %{srcname}-%{version} python2
cp -r python2 python3

%build
pushd python2
python2 setup.py build
popd

pushd python3
python setup.py build
popd

%install
pushd python2
python2 setup.py install --skip-build --root %{buildroot}
popd

pushd python3
python setup.py install --skip-build --root %{buildroot}
popd

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

%files -n python2-couchdb

