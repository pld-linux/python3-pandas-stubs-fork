Summary:	Type annotations for pandas
Summary(pl.UTF-8):	Adnotacje typów dla pandasa
Name:		python3-pandas-stubs-fork
Version:	1.5.3.230214
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pandas-stubs-fork/
Source0:	https://files.pythonhosted.org/packages/source/p/pandas-stubs-fork/pandas-stubs-fork-%{version}.tar.gz
# Source0-md5:	1a8ad4a1e1c062cead289f8059d8fafb
URL:		https://pypi.org/project/pandas-stubs-fork/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are public type stubs for pandas (<http://pandas.pydata.org/>),
following the convention of providing stubs in a separate package, as
specified in PEP 561. The stubs cover the most typical use cases of
pandas. In general, these stubs are narrower than what is possibly
allowed by pandas, but follow a convention of suggesting best
recommended practices for using pandas.

%description -l pl.UTF-8
Ten pakiet zawiera zaślepki publicznych typów dla modułu pandas
(<http://pandas.pydata.org/>), zgodne z konwencją dostarczania
zaślepek w osobnym pakiecie, przedstawioną w PEP 561. Zaślepki
pokrywają większość typowych przypadków użycia pandasa. W ogólności są
bardziej zawężone niż to, co jest dopuszczalne w pandasie, ale są
zgodne z konwencją sugerowania najlepszych praktyk użycia.

%prep
%setup -q -n pandas-stubs-fork-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pandas-stubs
%{py3_sitescriptdir}/pandas_stubs_fork-%{version}-py*.egg-info
